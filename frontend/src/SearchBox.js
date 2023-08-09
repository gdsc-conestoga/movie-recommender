import React, {useState} from "react";

function SearchBox({onSearch}) {
    const [searchText, setSearchText] = useState("");

    const handleSearch = async () => {
        const response = await fetch(`http://192.168.1.69/api/recommendation?title=${searchText}`);
        const data = await response.json();
        onSearch(data.movies);
    }

    return (
    <div className="search-box">
        <input type="text" value={searchText} onChange={(e) => setSearchText(e.target.value)} placeholder="Enter a movie!"/>
        <button onClick={handleSearch}>Search</button>
    </div>
        );

}

export default SearchBox;