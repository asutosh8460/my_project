<template>
    <div>
      <video ref="videoPlayer" controls @timeupdate="handleTimeUpdate">
        <track v-for="(subtitle, index) in subtitles" :key="index" :src="subtitle.src" :default="subtitle.default" kind="subtitles" srclang="en" label="English">
      </video>
      <div>{{ currentSubtitle.text }}</div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      subtitles: Array // Array of subtitle objects with src and default properties
    },
    data() {
      return {
        currentSubtitle: { text: "", timestamp: 0 },
        currentSubtitleIndex: -1
      };
    },
    methods: {
      handleTimeUpdate(event) {
        const currentTime = this.$refs.videoPlayer.currentTime;
  
        // Find the index of the current subtitle
        for (let i = this.subtitles.length - 1; i >= 0; i--) {
          if (currentTime >= this.subtitles[i].timestamp) {
            this.currentSubtitleIndex = i;
            this.currentSubtitle = this.subtitles[i];
            break;
          }
        }
      }
    }
  };
  </script>
  