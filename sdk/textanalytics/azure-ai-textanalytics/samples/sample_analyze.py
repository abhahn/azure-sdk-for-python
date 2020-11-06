# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_text.py

DESCRIPTION:
    This sample demonstrates how to submit a collection of text documents for analysis, which consists of a variety
    of text analysis tasks, such as Entity Recognition, PII Entity Recognition, Entity Linking, Sentiment Analysis,
    or Key Phrase Extraction.  The response will contain results from each of the individual tasks specified in the request.

USAGE:
    python sample_analyze_text.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your Text Analytics subscription key
"""


import os


class AnalyzeSample(object):

    def analyze(self):
        # [START analyze]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.textanalytics import TextAnalyticsClient, \
            EntitiesRecognitionTask, \
            PiiEntitiesRecognitionTask, \
            KeyPhraseExtractionTask

        endpoint = os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"]
        key = os.environ["AZURE_TEXT_ANALYTICS_KEY"]

        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=AzureKeyCredential(key),
            api_version="v3.1-preview.3"
        )

        documents = [
            "I had a wonderful trip to Seattle last week.",
            "I'm flying to NYC tomorrow. See you there."
        ]

        poller = text_analytics_client.begin_analyze(
            documents,
            display_name="Sample Text Analysis",
            entities_recognition_tasks=[EntitiesRecognitionTask()],
            pii_entities_recognition_tasks=[PiiEntitiesRecognitionTask()],
            key_phrase_extraction_tasks=[KeyPhraseExtractionTask()]
        )

        result = poller.result()

        for page in result:
            for task in page.entities_recognition_results:
                print("Results of task '{}':".format(task.name))
                
                docs = [doc for doc in task.results if not doc.is_error]
                for idx, doc in enumerate(docs):
                    print(type(doc))
                    print("\nDocument text: {}".format(documents[idx]))
                    for entity in doc.entities:
                        print("Entity: {}".format(entity.text))
                        print("...Category: {}".format(entity.category))
                        print("...Confidence Score: {}".format(entity.confidence_score))
                        print("...Offset: {}".format(entity.offset))
                    print("------------------------------------------")

            for task in page.pii_entities_recognition_results:
                print("Results of task '{}':".format(task.name))

                docs = [doc for doc in task.results if not doc.is_error]
                for idx, doc in enumerate(docs):
                    print("Document text: {}".format(documents[idx]))
                    for entity in doc.entities:
                        print("Entity: {}".format(entity.text))
                        print("Category: {}".format(entity.category))
                        print("Confidence Score: {}\n".format(entity.confidence_score))
                    print("------------------------------------------")

            for task in page.key_phrase_extraction_results:
                print("Results of task '{}':".format(task.name))

                docs = [doc for doc in task.results if not doc.is_error]
                for idx, doc in enumerate(docs):
                    print("Document text: {}\n".format(documents[idx]))
                    print("Key Phrases: {}\n".format(doc.key_phrases))
                    print("------------------------------------------")

        # [END analyze]


if __name__ == "__main__":
    sample = AnalyzeSample()
    sample.analyze()