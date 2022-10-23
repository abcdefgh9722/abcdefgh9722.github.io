window.onload = function () {
	let getEl = document.getElementsByClassName.bind(document);
	let pointer = getEl('pointer')[0];
	let result = '';
	let lights = Array.prototype.slice.call(getEl('light'));
	console.log(lights)

	// 记录当前是否正在旋转，如果当前正在旋转就不能点击
	let onRotation = false;
	let getReward = (function () {
		let currentDeg = 0;
		return function () {
			// 旋转3~4圈
			let rotateDeg = Math.random() * 360 + 1080;
			currentDeg += rotateDeg;
			let rewardText = window.texts[Math.floor((currentDeg + 18) % 360 / 36)];
			return {
				deg: currentDeg,
				text: rewardText === '谢谢参与'? '很遗憾你没有获得奖品' : '这顿吃'+rewardText
			}
		}
	})();

	pointer.addEventListener('click', () => {
		if (onRotation) {
			return;
		}
		console.log('开始抽奖');
		onRotation = true;
		lights.forEach(item => {
			item.className += ' light-twinkling';
		});
		let nextStatus = getReward();
		console.log(nextStatus);
		result = nextStatus.text;
		pointer.style.transform = `rotateZ(${nextStatus.deg}deg)`;
	});

	pointer.addEventListener('transitionend', () => {
		console.log('抽奖结束');
		// 等待闪烁三下结束
		setTimeout(() => {
			onRotation = false;
			lights.forEach(item => item.className = 'light');
			alert(result);
		}, 300);
	})
};

