# rss2youtube-dl

## Usage
    rss2youtube-dl
    Desc: A utility that downloads and parses rss feeds for videos to download with youtube-dl
    v.1.0
    2020 by radicalarchivist

    Usage:
        rss2youtube-dl [-CDhid] [-c CONFIGFILE] [-r CHANNEL]
        rss2youtube-dl --help
        rss2youtube-dl --version

    Options:
        -c --config CONFIGFILE                Use custom configuration file             
        -C --cron                             Script being run by cron, don't be interactive.
        -d --demo                             Don't save or add to seen
        -D --debug                            Print debug info to screen.
        -i --interactive                      Interactive mode
        -r --rss-from-channel CHANNEL         Get rss url for youtube channel url provided
        -h --help                             Show this screen
        --version                             Show version info

## .channels.yaml
    example:
        name: Feed Name (required)
        download_dir: /path/to/save/directory (required if not using filter directories)
        rss: https://rss.feed.url.com/.rss (required)
        filter: 
            - "Case Sensitive Filter (title filter)":
                download_dir: /path/to/save/dir (optional)