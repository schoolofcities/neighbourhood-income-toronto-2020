<script>
	import logo from '../assets/top-logo.svg'
</script>

<div id="bar">
	<a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
</div>

<style>
	#bar {
		position: fixed;
   		top: 0px;
		height: 50px;
		background-color: #fff9f4;
		margin-bottom: 20px;
		border-bottom: 1px solid rgb(255, 255, 255);
		width: 100%;
		min-width: 200px;
		padding-left: 0px;
		padding-right: 0px;
		text-align: center;
		z-index: 5;
		opacity: 0.95;
		box-shadow: 0 1px 0 0 rgba(227, 227, 227, 0.268);
	}
	img {
		color: blue;
	}
	img:hover {
		opacity: 0.7;
		cursor: pointer;
	}
</style>
