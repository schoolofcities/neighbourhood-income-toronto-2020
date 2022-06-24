<script>
	import { geoPath, geoMercator } from "d3";
	export let dataset = [];
	import { draw } from "svelte/transition";
	import { quadInOut } from "svelte/easing";
	
	const projection = geoMercator()
	.center([-79.42, 43.73])
	.scale([75000])
	.angle([-17]);
	const path = geoPath(projection);
  </script>
  
  {#each dataset as data}
	<path id="ct"
	  transition:draw={{ duration: 5000, delay: 0, easing: quadInOut }}
	  d={path(data)} fill="grey" 
	/>
  {/each}
  
  <style>
	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
  </style>