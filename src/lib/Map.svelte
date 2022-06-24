<script>
	import inc1961 from "../data/1961.geo.json";
	import formerMun from "../data/formerMun5.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export const year = "1961";

	const avgInc = {
		"1961": 4306.65
	}

	const projection = geoMercator()
		.center([-79.31, 43.76])
		.scale([75000])
		.angle([-17]);
	const path = geoPath(projection);

	let tracts = inc1961.features;

	const width = 800,
		height = 550;

	var color = scaleThreshold()
    .domain([avgInc[year] * 0.6, avgInc[year] * 0.8, avgInc[year] * 1.2, avgInc[year] * 1.4	])
    .range(['#DC4633','#e89a91','#ece2b8','#7bccc0','#00a189']);

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
		border: solid 1px rgb(0, 255, 170)	}
	#meow {
		border: solid 1px black;
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
