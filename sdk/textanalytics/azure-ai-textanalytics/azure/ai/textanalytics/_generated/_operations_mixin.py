# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
from msrest import Serializer, Deserializer
from typing import TYPE_CHECKING
import warnings

# FIXME: have to manually reconfigure import path for multiapi operation mixin
from .._lro import AnalyzeBatchActionsLROPoller, AnalyzeBatchActionsLROPollingMethod, AnalyzeHealthcareEntitiesLROPoller, AnalyzeHealthcareEntitiesLROPollingMethod
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union


class TextAnalyticsClientOperationsMixin(object):

    def analyze_status(
        self,
        job_id,  # type: str
        show_stats=None,  # type: Optional[bool]
        top=20,  # type: Optional[int]
        skip=0,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        """Get analysis status and results.

        Get the status of an analysis job.  A job may consist of one or more tasks.  Once all tasks are
        completed, the job will transition to the completed state and results will be available for
        each task.

        :param job_id: Job ID for Analyze.
        :type job_id: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param top: (Optional) Set the maximum number of results per task. When both $top and $skip are
         specified, $skip is applied first.
        :type top: int
        :param skip: (Optional) Set the number of elements to offset in the response. When both $top
         and $skip are specified, $skip is applied first.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeJobState, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_4.models.AnalyzeJobState
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('analyze_status')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'analyze_status'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.analyze_status(job_id, show_stats, top, skip, **kwargs)

    def begin_analyze(
        self,
        body=None,  # type: Optional["_models.AnalyzeBatchInput"]
        **kwargs  # type: Any
    ):
        """Submit analysis job.

        Submit a collection of text documents for analysis. Specify one or more unique tasks to be
        executed.

        :param body: Collection of documents to analyze and tasks to execute.
        :type body: ~azure.ai.textanalytics.v3_1_preview_4.models.AnalyzeBatchInput
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AnalyzeBatchActionsLROPollingMethod polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AnalyzeBatchActionsLROPoller that returns either AnalyzeJobState or the result of cls(response)
        :rtype: ~...._lro.AnalyzeBatchActionsLROPoller[~azure.ai.textanalytics.v3_1_preview_4.models.AnalyzeJobState]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_analyze')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_analyze'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_analyze(body, **kwargs)

    def begin_cancel_health_job(
        self,
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        """Cancel healthcare prediction job.

        Cancel healthcare prediction job.

        :param job_id: Job ID.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the LROBasePolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_cancel_health_job')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_cancel_health_job'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_cancel_health_job(job_id, **kwargs)

    def begin_health(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        string_index_type=None,  # type: Optional[Union[str, "_models.StringIndexType"]]
        **kwargs  # type: Any
    ):
        """Submit healthcare analysis job.

        Start a healthcare analysis job to recognize healthcare related entities (drugs, conditions,
        symptoms, etc) and their relations.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_4.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_4.models.StringIndexType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AnalyzeHealthcareEntitiesLROPollingMethod polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AnalyzeHealthcareEntitiesLROPoller that returns either HealthcareJobState or the result of cls(response)
        :rtype: ~...._lro.AnalyzeHealthcareEntitiesLROPoller[~azure.ai.textanalytics.v3_1_preview_4.models.HealthcareJobState]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_health')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_health'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_health(documents, model_version, string_index_type, **kwargs)

    def entities_linking(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Linked entities from a well-known knowledge base.

        The API returns a list of recognized entities with links to a well-known knowledge base. See
        the :code:`<a href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for
        the list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_0.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain input and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EntityLinkingResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_0.models.EntityLinkingResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('entities_linking')
        if api_version == 'v3.0':
            from .v3_0.operations import TextAnalyticsClientOperationsMixin as OperationClass
        elif api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'entities_linking'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.entities_linking(documents, model_version, show_stats, **kwargs)

    def entities_recognition_general(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Named Entity Recognition.

        The API returns a list of general named entities in a given document. For the list of supported
        entity types, check :code:`<a href="https://aka.ms/taner">Supported Entity Types in Text
        Analytics API</a>`. See the :code:`<a href="https://aka.ms/talangs">Supported languages in Text
        Analytics API</a>` for the list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_0.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain input and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EntitiesResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_0.models.EntitiesResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('entities_recognition_general')
        if api_version == 'v3.0':
            from .v3_0.operations import TextAnalyticsClientOperationsMixin as OperationClass
        elif api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'entities_recognition_general'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.entities_recognition_general(documents, model_version, show_stats, **kwargs)

    def entities_recognition_pii(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        domain=None,  # type: Optional[str]
        string_index_type=None,  # type: Optional[Union[str, "_models.StringIndexType"]]
        pii_categories=None,  # type: Optional[List[Union[str, "_models.PiiCategory"]]]
        **kwargs  # type: Any
    ):
        """Entities containing personal information.

        The API returns a list of entities with personal information (\"SSN\", \"Bank Account\" etc) in
        the document. For the list of supported entity types, check :code:`<a
        href="https://aka.ms/tanerpii">Supported Entity Types in Text Analytics API</a>`. See the
        :code:`<a href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the
        list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_4.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param domain: (Optional) if specified, will set the PII domain to include only a subset of the
         entity categories. Possible values include: 'PHI', 'none'.
        :type domain: str
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_4.models.StringIndexType
        :param pii_categories: (Optional) describes the PII categories to return.
        :type pii_categories: list[str or ~azure.ai.textanalytics.v3_1_preview_4.models.PiiCategory]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PiiResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_4.models.PiiResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('entities_recognition_pii')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'entities_recognition_pii'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.entities_recognition_pii(documents, model_version, show_stats, domain, string_index_type, pii_categories, **kwargs)

    def health_status(
        self,
        job_id,  # type: str
        top=20,  # type: Optional[int]
        skip=0,  # type: Optional[int]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Get healthcare analysis job status and results.

        Get details of the healthcare prediction job specified by the jobId.

        :param job_id: Job ID.
        :type job_id: str
        :param top: (Optional) Set the maximum number of results per task. When both $top and $skip are
         specified, $skip is applied first.
        :type top: int
        :param skip: (Optional) Set the number of elements to offset in the response. When both $top
         and $skip are specified, $skip is applied first.
        :type skip: int
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HealthcareJobState, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_4.models.HealthcareJobState
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('health_status')
        if api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'health_status'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.health_status(job_id, top, skip, show_stats, **kwargs)

    def key_phrases(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Key Phrases.

        The API returns a list of strings denoting the key phrases in the input text. See the :code:`<a
        href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the list of
        enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_0.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain input and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: KeyPhraseResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_0.models.KeyPhraseResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('key_phrases')
        if api_version == 'v3.0':
            from .v3_0.operations import TextAnalyticsClientOperationsMixin as OperationClass
        elif api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'key_phrases'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.key_phrases(documents, model_version, show_stats, **kwargs)

    def languages(
        self,
        documents,  # type: List["_models.LanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Detect Language.

        The API returns the detected language and a numeric score between 0 and 1. Scores close to 1
        indicate 100% certainty that the identified language is true. See the :code:`<a
        href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the list of
        enabled languages.

        :param documents:
        :type documents: list[~azure.ai.textanalytics.v3_0.models.LanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain input and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LanguageResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_0.models.LanguageResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('languages')
        if api_version == 'v3.0':
            from .v3_0.operations import TextAnalyticsClientOperationsMixin as OperationClass
        elif api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'languages'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.languages(documents, model_version, show_stats, **kwargs)

    def sentiment(
        self,
        documents,  # type: List["_models.MultiLanguageInput"]
        model_version=None,  # type: Optional[str]
        show_stats=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        """Sentiment.

        The API returns a sentiment prediction, as well as sentiment scores for each sentiment class
        (Positive, Negative, and Neutral) for the document and each sentence within it. See the
        :code:`<a href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the
        list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_0.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain input and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SentimentResponse, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_0.models.SentimentResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('sentiment')
        if api_version == 'v3.0':
            from .v3_0.operations import TextAnalyticsClientOperationsMixin as OperationClass
        elif api_version == 'v3.1-preview.4':
            from .v3_1_preview_4.operations import TextAnalyticsClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'sentiment'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.sentiment(documents, model_version, show_stats, **kwargs)
