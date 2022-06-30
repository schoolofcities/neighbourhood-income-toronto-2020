<script>
	import formerMun from "../data/formerMun.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export var year;
	export var tracts;
	export var colours;
	export var variable;

	const avgInc = {
		"1960": 4307,
		"1970": 11748,
		"1980": 27476,
		"1990": 54601,
		"2000": 69125,
		"2010": 87038,
		"2020": 102721 , // actually 2016
	};

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = (innerWidth * 40) / 80;

	$: projection = geoMercator()
		.center([-78.91, 43.64])
		.scale([38000])
		.angle([-17]);
	$: path = geoPath(projection);

	var color = scaleThreshold()
		.domain([
			avgInc[year] * 0.7,
			avgInc[year] * 0.85,
			avgInc[year] * 1.15,
			avgInc[year] * 1.3,
		])
		.range(colours);

	tracts.map((item) => {
		item.properties[variable]
			? (item.properties.color = color(item.properties[variable]))
			: (item.properties.color = "white");
	});
</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	<svg width={innerWidth} {height}>
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}

		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color} />
		{/each}

		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}

		<text id="year-label" x="5" y="22">{year}</text>
	</svg>
</div>

<style>
	#container {
		width: 100%;
		max-width: 800px;
		min-width: 400px;
	}

	#fm-back {
		stroke: rgb(0, 0, 0);
		stroke-width: 5px;
		opacity: 0.08;
		fill-opacity: 0;
	}
	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
	#fm {
		stroke: rgb(36, 36, 36);
		stroke-width: 1 px;
		fill-opacity: 0;
	}

	#year-label {
		font-size: 14px;
		fill: rgb(103, 103, 103);
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
</style>
