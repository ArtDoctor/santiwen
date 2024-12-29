<script lang="ts">
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	import github from '$lib/images/github.svg';
  </script>
  
  <header class="bg-gray-900 border-b border-gray-800">
	<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
	  <div class="flex justify-between items-center h-16">
		<!-- Logo Corner -->
		<div class="flex-shrink-0 w-12 h-12">
		  <a href="https://svelte.dev/docs/kit" 
			 class="flex items-center justify-center w-full h-full p-2 rounded-lg 
					hover:bg-gray-800 transition-colors">
			<img src={logo} alt="SvelteKit" class="w-full h-full object-contain" />
		  </a>
		</div>
  
		<!-- Navigation -->
		<nav class="flex-1 flex justify-center">
		  <ul class="flex space-x-1">
			<li>
			  <a
				href="/"
				class="px-4 py-2 rounded-lg text-sm font-medium transition-colors
					   {$page.url.pathname === '/' ? 
						 'bg-gray-800 text-white' : 
						 'text-gray-300 hover:bg-gray-800 hover:text-white'}"
				aria-current={$page.url.pathname === '/' ? 'page' : undefined}
			  >
				Home
			  </a>
			</li>
			<li>
			  <a
				href="/about"
				class="px-4 py-2 rounded-lg text-sm font-medium transition-colors
					   {$page.url.pathname === '/about' ? 
						 'bg-gray-800 text-white' : 
						 'text-gray-300 hover:bg-gray-800 hover:text-white'}"
				aria-current={$page.url.pathname === '/about' ? 'page' : undefined}
			  >
				About
			  </a>
			</li>
			<li>
			  <a
				href="/reader"
				class="px-4 py-2 rounded-lg text-sm font-medium transition-colors
					   {$page.url.pathname.startsWith('/reader') ? 
						 'bg-gray-800 text-white' : 
						 'text-gray-300 hover:bg-gray-800 hover:text-white'}"
				aria-current={$page.url.pathname.startsWith('/reader') ? 'page' : undefined}
			  >
				Reader
			  </a>
			</li>
		  </ul>
		</nav>
  
		<!-- Corner -->
		<!-- <div class="flex-shrink-0 w-12 h-12">
		</div> -->
	  </div>
	</div>
  </header>
  
  <style lang="postcss">
	/* Optional: Add any custom styles that can't be handled by Tailwind */
	@keyframes fadeIn {
	  from { opacity: 0; }
	  to { opacity: 1; }
	}
  
	header {
	  animation: fadeIn 0.3s ease-in-out;
	}
  </style>