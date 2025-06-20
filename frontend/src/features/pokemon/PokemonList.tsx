import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchData } from "../../services/api";

type Pokemon = {
    api_id: number;
    name: string;
    types: string;
    image_url: string;
}

export default function PokemonList() {
    const [pokemons, setPokemons] = useState<Pokemon[]>([]);

    useEffect(() => {
        fetchData<Pokemon[]>("http://localhost:8000/api/pokemon/")
            .then(setPokemons);
    }, []);

    return (
        <div>
            <h2>Pokémon List</h2>
            <ul>
                {pokemons.map((p) => (
                    <li key={p.api_id}>
                        <Link to={`/pokemon/${p.api_id}`}>{p.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    )
}