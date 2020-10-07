import functools
from urllib.parse import urlparse, parse_qsl
from azure.core.paging import AsyncItemPaged
from ._response_handlers import healthcare_result, analyze_result

async def healthcare_extract_page_data_async(response, obj, response_headers, health_job_state):
    return health_job_state.next_link, healthcare_result(response, health_job_state.results, response_headers, lro=True)


async def analyze_extract_page_data_async(response, obj, response_headers, analyze_job_state):
    return analyze_job_state.next_link, analyze_result(response, obj, response_headers, analyze_job_state.tasks)


async def lro_get_next_page_async(lro_status_callback, first_page, continuation_token):
    if continuation_token is None:
        return first_page

    try:
        continuation_token = continuation_token.decode("utf-8")

    except AttributeError:
        pass 

    parsed_url = urlparse(continuation_token)
    job_id = parsed_url.path.split("/")[-1]
    query_params = dict(parse_qsl(parsed_url.query.replace("$", "")))

    return await lro_status_callback(job_id, **query_params)
    

async def healthcare_paged_result_async(health_status_callback, response, obj, response_headers, show_stats=False):
    return await AsyncItemPaged(
        functools.partial(lro_get_next_page_async, health_status_callback, obj),
        functools.partial(healthcare_extract_page_data_async, response, obj, response_headers)
    )


async def analyze_paged_result_async(analyze_status_callback, response, obj, response_headers):
    return await AsyncItemPaged(
        functools.partial(lro_get_next_page_async, analyze_status_callback, obj),
        functools.partial(analyze_extract_page_data_async, response, obj, response_headers)
    )