<script>
	import inc1961 from "../data/1961.geo.json";
	import formerMun from "../data/formerMun5.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export const year = "1961";

	const avgInc = {
		"1961": 4306.65
	}

	const width = 800,
		height = 550;

	const projection = geoMercator()
		.center([-79.31, 43.76])
		.scale([75000])
		.angle([-17]);
	const path = geoPath(projection);

	let tracts = inc1961.features;

	var color = scaleThreshold()
    .domain([avgInc[year] * 0.6, avgInc[year] * 0.8, avgInc[year] * 1.2, avgInc[year] * 1.4	])
    .range(['#DC4633','#e89a91','#e6e3d6','#bed9dd','#6FC7EA']);

	['#DC4633','#e89a91','#e6e3d6','#7bccc0','#00a189']

	
	tracts.map(item => {item.properties.avg_inc ? item.properties.color = color(item.properties.avg_inc) : item.properties.color = "white"});

</script>

	<svg {width} {height} id="meow">
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)}/>
		{/each}
		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color}	/>
		{/each}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)}/>
		{/each}
	</svg>

<style>
	
	#meow {
		border: solid 1px black;
	}

	#fm-back {
		stroke: rgb(0, 0, 0);
		stroke-width: 5px;
		opacity: 0.1;
		fill-opacity: 0;
	}
	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
	#fm {
		stroke: rgb(59, 59, 59);
		stroke-width: 1	px;
		fill-opacity: 0;
	}
</style>
