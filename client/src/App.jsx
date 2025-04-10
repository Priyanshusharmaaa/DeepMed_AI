import './app.css';
import logo from './assets/Logo.png';

function App() {
  const openChat = () => {
    window.location.href = "http://localhost:8501";
  };

  const openDiagnose = () => {
    window.location.href = "http://localhost:8502"; 
  };

  const openGenerate = () => {
    window.location.href = "http://localhost:8503"; 
  };

  return (
    <>
      <div id="navbar">
        <img src={logo} alt="logo" className='logo' />
        <ul className='nav-buttons'>
          <li onClick={openChat} className='chatNav'>Chat</li>
          <li onClick={openDiagnose}>Diagnose</li>
          <li onClick={openGenerate}>Generate</li> {/* ✅ Added Generate Button */}
        </ul>
      </div>

      <div className='body1'>
        <div className='overlay'>
          <h1>
            <span className="fade-in fade-delay-1">Revolutionizing <span className="gradient-text">Diagnosis</span></span> <br />
            <span className="fade-in fade-delay-2">With</span> <br />
            <span className="fade-in fade-delay-3"><span className="gradient-text">AI</span> Precision</span>
          </h1>
        </div>
      </div>
    </>
  );
}

export default App;
