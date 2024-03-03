import React from "react";
import "./LandingPage.css";
import "./circular-charge.css";
import apple from "./assets/apple.png";
import banana from "./assets/banana.png";
import grape from "./assets/grape.png";
import pumpkin from "./assets/pumpkin.png";
import carrot from "./assets/carrot.png";
import steak from "./assets/steak.png";
import chicken from "./assets/chicken.png";
import fish from "./assets/fish.png";
import { useNavigate } from "react-router-dom";

const LandingPage = () => {
  const navigate = useNavigate();

  function handleClick() {
    navigate('/spin');
  }

  return (
  <div class="page-wrapper">
    <div class="slider">
      <div class="slide-track">
        <div class="slide">
        <img class="icon" src={apple}></img>
        </div>
        <div class="slide">
        <img class="icon" src={grape}></img>
        </div>
        <div class="slide">
        <img class="icon" src={banana}></img>
        </div>
        <div class="slide">
        <img class="icon" src={pumpkin}></img>
        </div>
        <div class="slide">
        <img class="icon" src={steak}></img>
        </div>
        <div class="slide">
        <img class="icon" src={carrot}></img>
        </div>
        <div class="slide">
        <img class="icon" src={chicken}></img>
        </div>
        <div class="slide">
        <img class="icon" src={fish}></img>
        </div>
      </div>
    </div>
    
    <div class="middle-section">
      <div class="project-title">
        <p class="recipe-roulette">RECIPE ROULETTE</p>
        <p class="discount">Meals made cheap</p>
      </div>
      <div class="button-container">
        <button class="btn-87" onClick={handleClick}>
          <span>Spin for recipes</span>
          <svg aria-hidden><circle></circle></svg>
        </button>
      </div>
    </div>

    <div class="slider">
      <div class="slide-track">
      <div class="slide">
        <img class="icon" src={apple}></img>
        </div>
        <div class="slide">
        <img class="icon" src={grape}></img>
        </div>
        <div class="slide">
        <img class="icon" src={banana}></img>
        </div>
        <div class="slide">
        <img class="icon" src={pumpkin}></img>
        </div>
        <div class="slide">
        <img class="icon" src={steak}></img>
        </div>
        <div class="slide">
        <img class="icon" src={carrot}></img>
        </div>
        <div class="slide">
        <img class="icon" src={chicken}></img>
        </div>
        <div class="slide">
        <img class="icon" src={fish}></img>
        </div>
      </div>
    </div>
    
    
  </div>);
};

export default LandingPage;