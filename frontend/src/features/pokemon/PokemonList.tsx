import { useEffect, useState } from "react";

type Pokemon = {
    api_id: number;
    name: string;
    types: string;
    image_url: string;
}

export default function PokemonList() {
    const [pokemons, setPokemons] = useState<Pokemon[]>([]);

    useEffect(() => {
        fetch("http://localhost:8000/pokemon/")
            .then((response) => response.json())
            .then((data) => setPokemons(data));
    }, []);

    return (
        <div>
            <h2>Pokémon List</h2>
            <ul>
                {pokemons.map((p) => (
                    <li key={p.api_id}>
                        <img src={p.image_url} width="100" height="100"/>
                        <div>
                            <h3>{p.name}</h3>
                            <p>{p.types}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    )
}