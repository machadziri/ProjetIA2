using System;
using System.IO;
using Microsoft.ML;
using Microsoft.ML.Data;
using Microsoft.ML.Transforms.Text;

class SentimentData
{
    [LoadColumn(0)]
    public string Text { get; set; }

    [LoadColumn(1), ColumnName("Label")]
    public bool Sentiment { get; set; }
}

class SentimentPrediction : SentimentData
{
    [ColumnName("PredictedLabel")]
    public bool Prediction { get; set; }

    public float Probability { get; set; }  // Utilisation de la probabilité pour la confiance
}

class Program
{
    static void Main()
    {
        try
        {
            var mlContext = new MLContext();
            string dataPath = Path.Combine(Environment.CurrentDirectory, "sentiment_data.tsv");
            string modelPath = Path.Combine(Environment.CurrentDirectory, "sentiment_model.zip");

            // Charger les données
            Console.WriteLine("🔄 Chargement des données...");
            IDataView dataView = mlContext.Data.LoadFromTextFile<SentimentData>(
                dataPath, separatorChar: '\t', hasHeader: true);

            // Définir la pipeline
            var pipeline = mlContext.Transforms.Text.FeaturizeText("Features", nameof(SentimentData.Text))
                .Append(mlContext.BinaryClassification.Trainers.SdcaLogisticRegression(
                    labelColumnName: "Label", featureColumnName: "Features"));

            ITransformer model;

            // Vérifier si un modèle est déjà sauvegardé
            if (File.Exists(modelPath))
            {
                Console.WriteLine("🔄 Chargement du modèle existant...");
                model = mlContext.Model.Load(modelPath, out _);
            }
            else
            {
                Console.WriteLine("📊 Entraînement du modèle...");
                model = pipeline.Fit(dataView);
                mlContext.Model.Save(model, dataView.Schema, modelPath);
                Console.WriteLine("📁 Modèle entraîné et sauvegardé !");
            }

            // Créer un moteur de prédiction
            var engine = mlContext.Model.CreatePredictionEngine<SentimentData, SentimentPrediction>(model);

            // Validation du modèle (précision sur un jeu de test, si disponible)
            EvaluateModel(mlContext, model, dataView);

            // Boucle interactive pour tester des phrases
            while (true)
            {
                Console.Write("\nEntrez un texte pour analyser le sentiment (ou tapez 'exit' pour quitter) : ");
                string inputText = Console.ReadLine();

                if (inputText.ToLower() == "exit")
                    break;

                var testData = new SentimentData { Text = inputText };
                var result = engine.Predict(testData);

                Console.WriteLine($"Sentiment prédit : {(result.Prediction ? "Positif 😊" : "Négatif 😡")}");
                Console.WriteLine($"Score de confiance : {result.Probability:0.00}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Erreur : {ex.Message}");
        }
    }

    static void EvaluateModel(MLContext mlContext, ITransformer model, IDataView dataView)
    {
        // Évaluation du modèle avec des métriques comme la précision et le rappel
        Console.WriteLine("\n📊 Évaluation du modèle...");
        var predictions = model.Transform(dataView);
        var metrics = mlContext.BinaryClassification.Evaluate(predictions);

        Console.WriteLine($"Précision : {metrics.Accuracy:0.00}");
        Console.WriteLine($"AUC : {metrics.AreaUnderRocCurve:0.00}");
        Console.WriteLine($"F1 Score : {metrics.F1Score:0.00}");
    }
}
