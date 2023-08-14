<template>
    <div>
      <input type="file" accept="video/*" @change="uploadVideo">
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    methods: {
      async uploadVideo(event) {
        const file = event.target.files[0];
  
        // Create a FormData object to send the file
        const formData = new FormData();
        formData.append('video', file);
  
        try {
          // Make a POST request to the server
          const response = await axios.post('/upload_video', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
  
          if (response.data.message) {
            console.log(response.data.message);
            // You can show a success message to the user here
          } else {
            console.error('Error uploading video');
            // Handle error scenario
          }
        } catch (error) {
          console.error('Error uploading video:', error);
          // Handle error scenario
        }
      }
    }
  }
  </script>
  