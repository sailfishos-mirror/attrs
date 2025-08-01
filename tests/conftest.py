# SPDX-License-Identifier: MIT

from datetime import timedelta

import pytest

from hypothesis import HealthCheck, settings

from attr._compat import PY_3_10_PLUS, PY_3_14_PLUS


@pytest.fixture(name="slots", params=(True, False))
def _slots(request):
    return request.param


@pytest.fixture(name="frozen", params=(True, False))
def _frozen(request):
    return request.param


def pytest_configure(config):
    # HealthCheck.too_slow causes more trouble than good -- especially in CIs.
    settings.register_profile(
        "patience",
        settings(
            suppress_health_check=[HealthCheck.too_slow],
            deadline=timedelta(milliseconds=400),
        ),
    )
    settings.load_profile("patience")


collect_ignore = []
if not PY_3_10_PLUS:
    collect_ignore.extend(["test_pattern_matching.py"])
if not PY_3_14_PLUS:
    collect_ignore.extend(["test_forward_references.py"])
