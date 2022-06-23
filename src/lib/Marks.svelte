<script>
	import { geoPath, geoNaturalEarth1, geoMercator } from "d3";
	export let dataset = [];
	import { draw } from "svelte/transition";
	import { quadInOut } from "svelte/easing";
	
	const projection = geoMercator()
	.center([-79.42, 43.73])
	.scale([100000])
	.angle([-17]);
	const path = geoPath(projection);
  </script>
  
  {#each dataset as data}
	<path
	  transition:draw={{ duration: 5000, delay: 0, easing: quadInOut }}
	  d={path(data)}
	/>
  {/each}
  
  <style>
	path {
	  fill: none;
	  stroke: rgb(0, 0, 0);
	}
  </style>