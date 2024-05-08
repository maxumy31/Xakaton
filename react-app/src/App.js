import logo from './logo.svg';
import './App.css';
import Button from '@mui/material/Button';
import UnivRating from './Table'

async function fetchAsync (url = "https://localhost:5000/") {
              let response = await fetch(url);
              let data = await response.json();
              return data;
            }

function App() {
  return (
    <div className="App">
      <header className="App-header">
        
        
      </header>
      <body>
          <Button variant="contained"
          onClick={() => {
            fetchAsync ("https://localhost:5000/user") }}>Hello world</Button> 
          <UnivRating />
      </body>
    </div>
  );
}

export default App;
