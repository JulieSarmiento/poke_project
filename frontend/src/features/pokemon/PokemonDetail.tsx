import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchData } from "../../services/api";

type Pokemon = {
    api_id: number;
    name: string;
    types: string;
    image_url: string;
}

export default function PokemonDetail() {
    const { id } = useParams<{ id: string}>();
    const [pokemon, setPokemon] = useState<Pokemon | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        setLoading(true);
        setError(null);

        fetchData<Pokemon>(`http://localhost:8000/api/pokemon/${id}`)
            .then(setPokemon)
            .catch((err) => setError(err.message))
            .finally(() => setLoading(false));
    }, [id]);

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error: {error}</div>
    if (!pokemon) return <div>Pokemon not found</div>

    return (
        <div>
            <img src={pokemon.image_url} width="100" height="100"/>
            <h2>{pokemon.name}</h2>
            <p>Types: {pokemon.types}</p>
            <p>ID: {pokemon.api_id}</p>
        </div>
    )
}