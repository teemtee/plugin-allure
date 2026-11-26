# plugin-allure

The `allure` report plugin for [tmt](https://github.com/teemtee/tmt).

Allure 3 no longer reads the JUnit XML format. This plugin writes one
`*-result.json` file per result and per subresult into a results directory,
which is the format Allure 3 consumes.

## Installation

```shell
pip install tmt-plugin-allure
```

Or, from a checkout:

```shell
pip install -e .
```

Either way tmt picks the plugin up through the `tmt.plugin` entry point. No
configuration is needed.

## Usage

```yaml
report:
    how: allure
    directory: /tmp/allure-results
```

`directory` is optional. Without it the results are written into the report
step workdir, under `allure-results`.

Possible test results and their mapping to Allure statuses:

| tmt result | Allure status |
| --- | --- |
| `pass` | `passed` |
| `fail` | `failed` |
| `skip`, `info` | `skipped` |
| `error`, `warn`, `pending` | `broken` |

Logs recorded by a test are stored as attachments. A failure log is parsed
and stored in the `trace` field instead, as long as it can be read. An
unreadable or empty log becomes an attachment, or is left out.

## Timing

Allure needs a start and a stop for every result. tmt does not always record
both, so the plugin derives the missing piece from the duration. A result
with no timing information at all is reported as a point in time.

Timestamps and durations are accepted both as `datetime` and `timedelta`
instances, and as the text tmt wrote before 1.82. A timestamp without a
timezone is taken as UTC, which is what tmt assumes as well.

## Requirements

- Python 3.12 or newer
- tmt 1.81 or newer

## License

MIT