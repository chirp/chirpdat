# chirpdat

Share files of any size with Chirp and dat

## Setup

Install dependencies

```
npm install -g dat
pip install chirpdat
```

Create a ~/.chirprc file with you app key, secret and config.
You can get these from developers.chirp.io.

```
# ~/.chirprc
app_key = xXxXXxxxXXXxxXXXxXxXXxXxx
app_secret = xxXxXXXxXxxXXXxXXXXxXxXxxxXxxxXXxXxXxxxXXxXxXXxXxX
app_config = XxXXXXxXxXxxxXxxxXXxXxXxxxXXxXxXXxXxXxxXxXXxxxXXXxxXxx
```

## Usage

To share a folder

```
chirpdat -s ~/Pictures
```

The dat link will be transmitted using sound, so a recipient
must run the script specifying a folder to download the files to...

Download and sync a shared folder

```
chirpdat -d ~/Downloads/pix
```


## Advanced

If your input/output devices are not the default, you can set a specific
input/output device to use.

To list the available devices

```
chirpdat -l
```

To set the input to device index 3.

```
chirpdat -i 3 -d ~/Downloads/pix
```

To set the output to device index 2.

```
chirpdat -o 2 -s ~/Pictures
```
