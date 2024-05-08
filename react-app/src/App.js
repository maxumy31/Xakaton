import logo from './logo.svg';
import './App.css';
import Button from '@mui/material/Button';
import UnivRating from './Table'
import axios from 'axios'

async function fetchAsync (url = "http://localhost:5000/") {

            // Make a request for a user with a given ID
            //axios.get('https://localhost:5000/user')

            axios.get('http://localhost:5000/user/username', {
              name:"admin"
            })
            .then((response) => {
              console.log(response);
            }, (error) => {
              console.log(error);
            });
            }

function App() {
  return (
    <div className="App">
      <header className="App-header">
        
        
      </header>
      <body>
          <Button variant="contained"
          onClick={() => {
            fetchAsync ("http://localhost:5000/user") }}>Hello world</Button> 
          <UnivRating />
      </body>
    </div>
  );
}

export default App;
