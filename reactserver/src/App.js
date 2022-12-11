import './App.css';
// import React, { useState } from 'react';
import axios from 'axios';
  
import React,{Component} from 'react';
  
class App extends Component {
   
    state = {
      selectedFile: null
    };

    onFileChange = event => {

      this.setState({ selectedFile: event.target.files[0] });
     
    };
     
    onFileUpload = () => {
     
      // Create an object of formData
      const formData = new FormData();
     
      // Update the formData object
      formData.append(
        "video",
        this.state.selectedFile
      );
     
      // Details of the uploaded file
      console.log(this.state.selectedFile);
     
      // Request made to the backend api
      // Send formData object
      axios.post(" http://localhost:3001/summarize", formData);
    };
     
    // File content to be displayed after
    // file upload is complete
    fileData = () => {
     
      if (this.state.selectedFile) {
          
        return (
          <div>
            <h2>File Details:</h2>
            <p>File Name: {this.state.selectedFile.name}</p>
  
            <p>File Type: {this.state.selectedFile.type}</p>
  
            <p>
              Last Modified:{" "}
              {this.state.selectedFile.lastModifiedDate.toDateString()}
            </p>
  
          </div>
        );
      } else {
        return (
          <div>
            <br />
            <h4>Choose before Pressing the Upload button</h4>
          </div>
        );
      }
    };
     
    render() {
     
      return (
        <div>
            <div>
                <input type="file" onChange={this.onFileChange} />
                <button onClick={this.onFileUpload}>
                  Upload!
                </button>
            </div>
          {this.fileData()}
        </div>
      );
    }
  }
  
  export default App;