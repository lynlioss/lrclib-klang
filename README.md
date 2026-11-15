# LRCLIB for Klang

A lyric provider for [Klang](https://github.com/lynlioss/klang), using the free [LRCLIB](https://lrclib.net/) database.

## Install

In Klang, open Settings → Plugins → +, paste `https://github.com/lynlioss/lrclib-klang`, and install. Then enable LRCLIB.

Requires a Klang release with plugin API 1 support.

## What it does

Loads plain, line-synced, and word-synced lyrics when available. Includes offline caching and a timing adjustment setting. No account or API key is required. Opening lyrics sends song title, artist, album, and duration to LRCLIB.

`plugin.json` is the whole plugin. To publish an update, change its version, commit it, and run the Release workflow. Releases include `plugin.json` and its SHA-256 checksum.

To make your own provider, read [Klang's plugin guide](https://github.com/lynlioss/klang/blob/main/docs/plugins.md).

Licensed under GPL-3.0. LRCLIB is a separate community service.
