'use client'

import React, { useState, useEffect } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import logo from '@/public/images/logo/busy-bees-addis-logo.png'
import {
	playfairDisplay,
	playfairDisplayItalic,
	montserrat,
	oswald,
	raleway,
} from '@/styles/fonts'
import 'bootswatch/dist/sandstone/bootstrap.min.css'
import styles from '@/styles/navbar.module.css'

interface Links {
	links: string[]
	activeSection: string
}

export default function Navbar({ links, activeSection }: Links) {
	const [toggleMenu, setToggleMenu] = useState(false)
	const [isChecked, setIsChecked] = useState(false)
	const [screenWidth, setScreenWidth] = useState(1348)
	const [activeNav, setActiveNav] = useState(`#${activeSection}`)

	const handleClick = (href: string) => {
		setActiveNav(`#${href}`)
	}

	const toggleNav = () => {
		setToggleMenu(!toggleMenu)
		setIsChecked(!isChecked)
	}

	function screenTest() {
		if (window.innerWidth <= 868) {
			toggleNav()
		}
	}

	useEffect(() => {
		const changeWidth = () => {
			setScreenWidth(window.innerWidth)
		}
		window.addEventListener('resize', changeWidth)
		return () => {
			window.removeEventListener('resize', changeWidth)
		}
	}, [])

	return (
		<nav
			className={`${styles['custom-header']} navbar navbar-expand-md border-0 fixed-top`}
			data-bs-theme='dark'
		>
			<div className='container-fluid'>
				<Link className={`navbar-brand border-0 ${styles.brand}`} href='/'>
					<Image
						src={logo}
						alt='Busy Bees Addis Logo'
						className={styles.logo}
					/>
				</Link>
				<input
					id='menu__toggle'
					className={styles['menu__toggle']}
					type='checkbox'
					checked={isChecked}
					onChange={toggleNav}
				/>
				<label className={styles['menu__btn']} htmlFor='menu__toggle'>
					<span></span>
				</label>
				{(toggleMenu || screenWidth > 868) && (
					<div
						className={`text-center ${styles['menu__box']} ${raleway.className}`}
					>
						<ul className={`navbar-nav ms-auto border-0`}>
							{links.map((link, index) => (
								<li
									key={index}
									className={`nav-item me-1 ${styles['custom-nav-item']}`}
									onClick={() => handleClick(link)}
								>
									<Link
										href={`#${link}`}
										className={`nav-link border-start-0 border-end-0 ${
											activeNav === link || activeSection === link
												? styles.active
												: styles['menu__item']
										}`}
										onClick={screenTest}
									>
										{link === 'program' ? 'our program' : link}
									</Link>
								</li>
							))}
						</ul>
					</div>
				)}
			</div>
		</nav>
	)
}
