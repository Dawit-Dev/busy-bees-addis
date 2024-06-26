'use client'

import Image from 'next/image'
import AnimateCharacters from '@/animations/character-animation'

import { raleway } from '@/styles/fonts'
import styles from '@/styles/hero.module.css'

type HeroProps = {
	id: number
	logo: string
	hero_image: string
	brand: string
	motto: string
}

export default function Hero({ hero }: { hero: HeroProps }) {
	return (
		<section id='hero' className={styles.hero}>
			<div className={styles['hero-image-container']}>
				<Image
					alt='hero background'
					src={`https://res.cloudinary.com/${process.env.NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME}/${hero.hero_image}`}
					width={300}
					height={300}
					className={styles['hero-img']}
					sizes='100vw'
				/>
				<div className={`${styles.overlay}`}>
					<AnimateCharacters
						text={hero.brand}
						el='h1'
						delay={0.4}
						rotateX={360}
						duration={1}
						type='spring'
						stiffness={100}
						className={styles.brand}
						playfair
					/>
					<AnimateCharacters
						text={hero.motto.replace(/\b[a-z]/g, (x: string) =>
							x !== 'a' ? x.toUpperCase() : x
						)}
						el='h2'
						delay={1.4}
						duration={0.2}
						x={-40}
						className={`${styles.motto} ${raleway.className}`}
					/>
				</div>
			</div>
		</section>
	)
}
