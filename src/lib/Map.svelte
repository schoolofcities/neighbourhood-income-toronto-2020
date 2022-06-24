<script>	
	import inc1961 from "../data/1961.geo.json";
	import formerMun from "../data/formerMun.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export const year = "1961";

	const avgInc = {
		"1961": 4306.65,
	};

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = innerWidth * 40/80

	let c1 = [-79.29, 43.70]
	let c2 = [-78.89, 43.64]

	$: console.log(innerWidth)
	$: console.log([-0.004* innerWidth - 81.49, 0.00015 * innerWidth + 43.58 ])

	$: projection = geoMercator()
		.center([-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ])
		.scale([75000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);	

	let tracts = inc1961.features;

	var color = scaleThreshold()
		.domain([
			avgInc[year] * 0.6,
			avgInc[year] * 0.8,
			avgInc[year] * 1.2,
			avgInc[year] * 1.4,
		])
		.range(["#DC4633", "#e89a91", "#e6e3d6", "#bed9dd", "#6FC7EA"]);

	tracts.map((item) => {
		item.properties.avg_inc
			? (item.properties.color = color(item.properties.avg_inc))
			: (item.properties.color = "white");
	});
</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	<svg width={innerWidth} height={height} id="meow">
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}
		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color} />
		{/each}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}
	</svg>
</div>

<style>
	#container {
		/* margin: 0 auto; */
		/* padding-left: 0px; */
		width: 100%;
		max-width: 800px;
		min-width: 400px;
	}
	#meow {
		border: solid 1px rgb(217, 217, 217);
		/* border-radius: 5px; */
		border-bottom-right-radius: 100px;
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
		stroke: rgb(107, 107, 107);
		stroke-width: 1 px;
		fill-opacity: 0;
	}
</style>
