<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Youtube2image&fontSize=90" />

# youtube2image
downloader youtube video &amp; extract image by frame

## How to use
```
python run.py [-i] [-d] [-e] [-f height weight] [-c class_name]
```

```
Youtube video download & frames extraction, cropping, filtering, sampling tools

optional arguments:
  -h, --help        show this help message and exit
  -i                install requirement library
  -d                download video from youtube link in "list.txt", saving in 'src'
  -e                extract frames from 'src' directory
  -f height weight  filter images by given minimum size(height, weight)
  -c class_name     crop images by class name
  -s sample_number  sampling by given number of samples
  --force           If you have any data, they would be deleted
```

<br>(Please don't forget put youtube links in list.txt if you want to download youtube videos)

![Footer](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=footer)