<template>
    <div>
      <textarea v-model="subtitleText"></textarea>
      <button @click="addSubtitle">Add Subtitle</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        subtitleText: ""
      };
    },
    methods: {
      addSubtitle() {
        if (this.subtitleText.trim() === "") {
          return; // Don't add empty subtitles
        }
  
        const currentTime = this.$refs.videoPlayer.currentTime; // Get current video timestamp
        const newSubtitle = {
          text: this.subtitleText,
          timestamp: currentTime
        };
  
        // Emit an event to the parent component (App.vue) to handle the subtitle
        this.$emit("subtitle-added", newSubtitle);
  
        // Clear the subtitle text field
        this.subtitleText = "";
      }
    }
  }
  </script>
  