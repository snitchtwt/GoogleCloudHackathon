import "./App.css";
//components
import Todofrom from "./components/todoform";
import Currenttodo from "./components/currenttodo";
import Header from "./components/navigationbar";

function App() {
  return (
    <div className="App">
      <Header />
      <Todofrom />
      <Currenttodo />
    </div>
  );
}

export default App;
