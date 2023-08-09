import React from 'react';
import MovieCard from './MovieCard';

function MovieList ({movies}){
console.log(movies)
    if(!Array.isArray(movies)){
        return <div className="movie-list">No movies found!</div>;
    }

    return (
        <div className="movie-list">
            {movies.map((movie) => (
                <MovieCard key={movie.title} movie={movie}/>
            ))}
        </div>

        );

}

export default MovieList;