<script lang="ts">
  import { onMount } from 'svelte';
  import type { Sentence } from '$lib/types';
  
  let currentSentence: Sentence | null = null;
  let currentSentenceID: number = 0;
  let isDetailsVisible = false;
  let bucketWords: string[] = [];
  
  interface Word {
    chinese: string;
    pinyin: string;
    translation: string;
  }
  
  async function loadSentence() {
    try {
      const response = await fetch('http://127.0.0.1:8000/sentences/' + currentSentenceID);
      currentSentence = await response.json();
      isDetailsVisible = false;
      currentSentenceID++;
    } catch (error) {
      console.error('Failed to load sentence:', error);
    }
  }
  
  function handleDragStart(event: DragEvent, word: string) {
    if (event.dataTransfer) {
      event.dataTransfer.setData('text/plain', word);
    }
  }
  
  function handleDrop(event: DragEvent) {
    event.preventDefault();
    const word = event.dataTransfer?.getData('text/plain');
    if (word && !bucketWords.includes(word)) {
      bucketWords = [...bucketWords, word];
    }
  }
  
  function handleDragOver(event: DragEvent) {
    event.preventDefault();
  }
  
  function removeFromBucket(word: string) {
    bucketWords = bucketWords.filter(w => w !== word);
  }
  
  onMount(() => {
    loadSentence();
  });
</script>

<div class="container mx-auto p-4 max-w-4xl bg-gray-900 min-h-screen text-gray-100">
  <!-- Main sentence display -->
  {#if currentSentence}
    <div class="mb-8">
      <div class="text-3xl mb-4 text-white font-semibold">
        {currentSentence.chinese}
      </div>
      
      <button
        on:click={() => isDetailsVisible = !isDetailsVisible}
        class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg mr-4 transition-colors"
      >
        {isDetailsVisible ? 'Hide Details' : 'Show Details'}
      </button>
      
      <button
        on:click={loadSentence}
        class="bg-emerald-600 hover:bg-emerald-700 text-white px-4 py-2 rounded-lg transition-colors"
      >
        Next Sentence
      </button>
    </div>
    
    {#if isDetailsVisible}
      <div class="mb-8 space-y-4">
        <div class="text-xl text-gray-300">
          {currentSentence.pinyin}
        </div>
        <div class="text-xl text-gray-400">
          {currentSentence.translation}
        </div>
        
        <!-- Individual words -->
        <div class="flex flex-wrap gap-2">
          {#each currentSentence.words as word}
            <div
              draggable="true"
              on:dragstart={(e) => handleDragStart(e, word.chinese)}
              class="bg-gray-800 p-2 rounded cursor-move hover:bg-gray-700 
                     transition-colors border border-gray-700"
            >
              <div class="font-bold text-white">{word.chinese}</div>
              <div class="text-sm text-gray-300">{word.pinyin}</div>
              <div class="text-sm text-gray-400">{word.translation}</div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  {/if}
  
  <!-- Review bucket -->
  <div
    on:drop={handleDrop}
    on:dragover={handleDragOver}
    class="border-2 border-dashed border-gray-700 p-4 rounded-lg min-h-[100px]
           bg-gray-800/50 backdrop-blur-sm"
  >
    <h2 class="text-xl font-bold mb-4 text-white">Review Bucket</h2>
    <div class="flex flex-wrap gap-2">
      {#each bucketWords as word}
        <div 
          class="bg-amber-900/50 p-2 rounded flex items-center group
                 border border-amber-700/50"
        >
          <span class="text-amber-100">{word}</span>
          <button
            on:click={() => removeFromBucket(word)}
            class="ml-2 text-red-400 opacity-0 group-hover:opacity-100 
                   hover:text-red-300 transition-opacity"
          >
            ×
          </button>
        </div>
      {/each}
    </div>
  </div>
</div>