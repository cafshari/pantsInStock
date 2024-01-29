import pytest


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.6261.6 Safari/537.36',
        # user agents for playwright listed at: https://github.com/microsoft/playwright/blob/main/packages/playwright
        # -core/src/server/deviceDescriptorsSource.json
        'base_url': 'https://bananarepublic.gap.com'

    }
