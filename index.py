import chalk

white = chalk.Chalk('white')
print(white('foo', bold=True, underline=True))
# returns '\x1b[37;1;4mfoo\x1b[0m'

bold_white = white + chalk.utils.FontFormat('bold')
print(bold_white('foo'))
# returns '\x1b[37;1mfoo\x1b[0m'

print(bold_white + 'foo')
# returns '\x1b[37;1mfoo'

print(bold_white + 'foo' + chalk.RESET)
# returns '\x1b[37;1mfoo/x1b[0m'