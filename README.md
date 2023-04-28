[dotbot_repo]: https://github.com/anishathalye/dotbot

# dotbot zypper Plugin

Plugin for [Dotbot][dotbot_repo], that adds ```zypper``` directive, which allows you to install and upgrade packages using ```zypper``` from known sources or from configurable Repos.

## Installation

```
git submodule add https://gitlab.com/paulbecker/dotbot_plugin_zypper.git
```

## Usage

```yaml
- zypper:
    public_keys:
      - https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
    repositories:
      - https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
    packages:
      - fish
      - bottom
      - brave-browser
```
