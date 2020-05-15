# NOTICE: Generated By HttpRunner. DO'NOT EDIT!
from httprunner import HttpRunner, TConfig, TStep, TestCase


class TestCaseValidateWithVariables(TestCase):
    config = TConfig(
        **{
            "name": "request methods testcase: validate with variables",
            "variables": {"foo1": "session_bar1"},
            "base_url": "https://postman-echo.com",
            "verify": False,
            "path": "examples/postman_echo/request_methods/validate_with_variables_test.py",
        }
    )

    teststeps = [
        TStep(
            **{
                "name": "get with params",
                "variables": {"foo1": "bar1", "foo2": "session_bar2"},
                "request": {
                    "method": "GET",
                    "url": "/get",
                    "params": {"foo1": "$foo1", "foo2": "$foo2"},
                    "headers": {"User-Agent": "HttpRunner/3.0"},
                },
                "extract": {"session_foo2": "body.args.foo2"},
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.args.foo1", "$foo1"]},
                    {"eq": ["body.args.foo2", "$foo2"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "post raw text",
                "variables": {"foo1": "hello world", "foo3": "$session_foo2"},
                "request": {
                    "method": "POST",
                    "url": "/post",
                    "headers": {
                        "User-Agent": "HttpRunner/3.0",
                        "Content-Type": "text/plain",
                    },
                    "data": "This is expected to be sent back as part of response body: $foo1-$foo3.",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {
                        "eq": [
                            "body.data",
                            "This is expected to be sent back as part of response body: session_bar1-$foo3.",
                        ]
                    },
                ],
            }
        ),
        TStep(
            **{
                "name": "post form data",
                "variables": {"foo1": "bar1", "foo2": "bar2"},
                "request": {
                    "method": "POST",
                    "url": "/post",
                    "headers": {
                        "User-Agent": "HttpRunner/3.0",
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    "data": "foo1=$foo1&foo2=$foo2",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.form.foo1", "$foo1"]},
                    {"eq": ["body.form.foo2", "$foo2"]},
                ],
            }
        ),
    ]

    def test_start(self):
        HttpRunner(self.config, self.teststeps).run()
