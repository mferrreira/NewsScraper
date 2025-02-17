// src/components/NewsCard.jsx
import React from 'react'

export default function NewsCard({ title, description, url, imageUrl, source }) {
    // Definindo a cor da borda conforme a fonte da notícia
    const borderColor = source === 'UOL' ? 'bg-blue-100' :
                        source === 'G1' ? 'bg-blue-200' :  'bg-blue-300'

    return (
        <div className={`text-gray-900 justify-between border border-black ${borderColor} p-4 rounded-lg shadow-lg  max-w-md h-fit mb-4 break-inside-avoid-column	`}>
        <p className="text-xs text-gray-500 my-2">Fonte: {source}</p>
        {imageUrl && (
          <img
            src={imageUrl}
            alt={title}
            className="w-full h-32 object-cover mb-4 rounded"
          />
        )}
        <h3 className="text-xl font-semibold">{title}</h3>
        <p className="text-gray-100 text-sm">{description}</p>
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-500 mt-2 inline-block"
        >
          Leia mais
        </a>
        {/* Exibindo a fonte da notícia */}
      </div>
    );
}
