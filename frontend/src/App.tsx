import { Routes, Route } from "react-router-dom";
import PokemonList from "./features/pokemon/PokemonList";
import PokemonDetail from "./features/pokemon/PokemonDetail";

function App() {
  return (
    <Routes>
      <Route path="/" element={<PokemonList />} />
      <Route path="/pokemon/:id" element={<PokemonDetail />} />
    </Routes>
  )
}

export default App;
