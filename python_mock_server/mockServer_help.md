Usage: /home/ime/Build/mock_server/python_mock_server/venv/bin/mock-server [OPTIONS]

Options:

  --help                           show this help information

/home/ime/Build/mock_server/python_mock_server/venv/bin/mock-server options:

  --address                        run on the given address (default localhost)
  --application-data               Application data file (default
                                   application.json)
  --custom-provider                Custom response provider
  --debug                           (default False)
  --dir                            dir with api definitions
  --num-processes                  Number of child processes (default 1)
  --port                           run on the given port (default 8888)

/home/ime/Build/mock_server/python_mock_server/venv/lib/python3.8/site-packages/tornado/log.py options:

  --log-file-max-size              max size of log files before rollover
                                   (default 100000000)
  --log-file-num-backups           number of log files to keep (default 10)
  --log-file-prefix=PATH           Path prefix for log files. Note that if you
                                   are running multiple tornado processes,
                                   log_file_prefix must be different for each
                                   of them (e.g. include the port number)
  --log-rotate-interval            The interval value of timed rotating
                                   (default 1)
  --log-rotate-mode                The mode of rotating files(time or size)
                                   (default size)
  --log-rotate-when                specify the type of TimedRotatingFileHandler
                                   interval other options:('S', 'M', 'H', 'D',
                                   'W0'-'W6') (default midnight)
  --log-to-stderr                  Send log output to stderr (colorized if
                                   possible). By default use stderr if
                                   --log_file_prefix is not set and no other
                                   logging is configured.
  --logging=debug|info|warning|error|none 
                                   Set the Python log level. If 'none', tornado
                                   won't touch the logging configuration.
                                   (default info)

