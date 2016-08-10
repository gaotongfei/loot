# loot

`loot` is a command line tool that helps you work with github in terminal without pain.

Now `loot` only supports checking and downloading gist.

**More features are working in process.**

## Install

`pip install loot`

## Usage

use `loot --help` to check supported commands and options

## Examples

### gist

Show all gists that user gaotongfei created:

```
loot gist -u gaotongfei
```

Show all gists that user gaotongfei created that contains keyword: 'request' in gists' description and filename

```
loot gist -u gaotongfei -k request
```

Pretty print above result:

```
loot gist -u gaotongfei -k request -p
```

### clone

Download gist in your current directory by default:
```
loot clone 2e37d97e93619c07d0b2910e3c4034e5
```

(`2e37d97e93619c07d0b2910e3c4034e5` is gist id)

you can specify directory by using `--dir` or `-d`
