<template>
    <div id="app">
      <VideoUpload @video-uploaded="handleVideoUploaded" />
      <SubtitleEditor v-if="videoUploaded" @subtitle-added="handleSubtitleAdded" />
      <VideoPlayer v-if="videoUploaded" :subtitles="subtitles" />
    </div>
  </template>
  
  <script>
  import VideoUpload from "./components/VideoUpload.vue";
  import SubtitleEditor from "./components/SubtitleEditor.vue";
  import VideoPlayer from "./components/VideoPlayer.vue";
  
  export default {
    components: {
      VideoUpload,
      SubtitleEditor,
      VideoPlayer
    },
    data() {
      return {
        videoUploaded: false,
        subtitles: []
      };
    },
    methods: {
      handleVideoUploaded() {
        this.videoUploaded = true;
      },
      handleSubtitleAdded(subtitle) {
        this.subtitles.push(subtitle);
      }
    }
  };
  </script>
  