# What is this?
A command-line utility to retrieve and display Alexa site rankings for hostname(s).

Also exposes the getSiteRank and getSiteRanks methods for use as a module.

# Usage as a Command-line Utility
```bash
> python alexa_compare.py
Retrieves and displays Alexa rankings for a hostname.

  Usage: alexa_compare.py [Flags]... [Hostname]...

  Flags:
    --help | display this help information
    --json | output to json
```

# Example Command-Line Usage
```bash
> python alexa_compare.py --json github.com gitlab.com
[
  {
    "global_rank":53,
    "hostname":"github.com",
    "top_country":"China",
    "top_country_rank":50
  },
  {
    "global_rank":3696,
    "hostname":"gitlab.com",
    "top_country":"India",
    "top_country_rank":2243
  }
]
```
# Example Module Usage
```bash
> python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from alexa_compare import getSiteRanks
>>> print getSiteRanks('github.com','gitlab.com')
[{'global_rank': 53, 'top_country_rank': 50, 'hostname': 'github.com', 'top_country': 'China'}, {'global_rank': 3696, 'top_country_rank': 2243, 'hostname': 'gitlab.com', 'top_country': 'India'}]
```