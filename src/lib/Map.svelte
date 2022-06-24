<script>
	import inc1961 from "../data/1961.geo.json";
	import formerMun from "../data/formerMun5.geo.json";

	import { geoPath, geoMercator, scaleThreshold } from "d3";

	const projection = geoMercator()
		.center([-79.31, 43.76])
		.scale([75000])
		.angle([-17]);
	const path = geoPath(projection);

	let tracts = inc1961.features;

	const width = 800,
		height = 550;

	let values = tracts.map(item => item.properties.avg_inc);
	console.log(values)

	var color = scaleThreshold()
    .domain([5000,8000])
    .range(["red", "white", "green"]);


	tracts.map(item => {item.properties.color = color(item.properties.avg_inc)});

</script>

<main>
	<svg {width} {height} id="meow">
		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color}	/>
		{/each}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)}/>
		{/each}
	</svg>
</main>

<style>
	main {
		background-color: aquamarine;
	}
	#meow {
		background-color: antiquewhite;
	}

	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
	#fm {
		stroke: rgb(0, 0, 0);
		stroke-width: 1	px;
		fill-opacity: 0;
	}
</style>
