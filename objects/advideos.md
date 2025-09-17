---
title: Video (AdVideo) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/advideos
crawled_at: 2025-09-17T15:52:21.945424
---

Servicing
# Video (AdVideo)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos#service)
  * [Requirements for videos uploaded via the API](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos#requirements)


The Video object (AdVideo) contains a video.
An ad can only have one video (or none at all). You can assign the same video to multiple ads. For more information, see [Video extensions](https://yandex.com/support/direct/features/video-extension.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos#service)Servicing
The [AdVideos](https://yandex.com/dev/direct/doc/ref-v5/advideos/advideos.html) service is designed to perform operations with videos.
To synchronously upload videos by their URLs or as binary data, use the [add](https://yandex.com/dev/direct/doc/ref-v5/advideos/add.html) operation of the [AdVideos](https://yandex.com/dev/direct/doc/ref-v5/advideos/advideos.html) method.
The [Get](https://yandex.com/dev/direct/doc/ref-v5/advideos/get.html) operation returns the processing status of uploaded videos.
Video editing is not supported. If you need to edit a video, upload a new video and create a new video extension from it.
You can a create a video extension from a video using the [Creatives](https://yandex.com/dev/direct/doc/ref-v5/creatives/creatives.html) service. To add a video extension to an ad or remove it from an ad, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service. See [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign#harness).
A video undergoes moderation only when it is assigned to an ad. See [Result of reviewing add-ons](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos#requirements)Requirements for videos uploaded via the API
Format |  MP4, WebM, MOV, QT, FLV, AVI  
---|---  
Size |  Maximum 100 MB  
Duration |  From 5 to 60 s  
For non-skippable videos, the maximum video duration is 15 s.  
Aspect ratio |  3:1, 2:1, 1.9:1, 16:9, 4:3, 1.91:1, 1:1, 3:4, 4:5, 9:16, 1:2, 1:3  
Minimum resolution |  360p  
Recommended resolution |  1080p  
Video frame rate |  between 20 and 30 frames/second  
Video codecs |  H.264, VP6F, VP8, Theora  
Number of video tracks |  1  
Minimum quality |  44 kHz, 16 Kbit/s, stereo  
Audio codecs |  AAC, MP3, Vorbis  
Number of audio tracks |  0 or 1  
File codec |  avc1, F4V, isom, M4A, M4V, mp4, mp41, mp42, qt  
Cover |  No  
### Was the article helpful?
YesNo
Previous
[Image (AdImage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage)
Next
[Creative (Creative)](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative)
