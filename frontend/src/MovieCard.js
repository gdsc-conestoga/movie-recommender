import React from 'react';

function MovieCard({movie}){
    return (
        <a href={movie.url} className="movie-card">
            <h2> {movie.title}</h2>
            <img src={movie.poster_path} alt={movie.title}/>
            <p>{movie.release_date}</p>
            <p>{movie.popularity}</p>
            <p>{movie.vote_average}</p>
            <p>{movie.vote_count}</p>
        </a>
    );
}

export default MovieCard;