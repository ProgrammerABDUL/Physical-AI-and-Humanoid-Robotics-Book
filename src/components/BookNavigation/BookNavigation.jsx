import React from 'react';
import './BookNavigation.module.css';

const BookNavigation = () => {
  const modules = [
    {
      title: 'Weeks 1-2: Foundations',
      path: '/docs/week1-foundations',
      topics: ['Physical AI Principles', 'Sensors', 'Embodiment']
    },
    {
      title: 'Weeks 3-5: ROS 2',
      path: '/docs/week3-ros',
      topics: ['Nodes & Topics', 'URDF', 'Services', 'Launch Files']
    },
    {
      title: 'Weeks 6-7: Simulation',
      path: '/docs/week6-simulation',
      topics: ['Gazebo', 'Unity Digital Twin', 'Physics Simulation']
    },
    {
      title: 'Weeks 8-10: NVIDIA Isaac',
      path: '/docs/week8-isaac',
      topics: ['Isaac Sim', 'Perception', 'VSLAM', 'Manipulation']
    },
    {
      title: 'Weeks 11-12: Humanoid Robots',
      path: '/docs/week11-humanoid',
      topics: ['Locomotion', 'Manipulation', 'Control Systems']
    },
    {
      title: 'Week 13: VLA & Multimodal',
      path: '/docs/week13-multimodal',
      topics: ['Vision-Language-Action', 'GPT Robotics', 'Whisper Integration']
    }
  ];

  return (
    <div className="book-navigation-container">
      <h2>Course Navigation</h2>
      <div className="modules-grid">
        {modules.map((module, index) => (
          <div key={index} className="module-card">
            <h3>
              <a href={module.path}>{module.title}</a>
            </h3>
            <ul className="topics-list">
              {module.topics.map((topic, topicIndex) => (
                <li key={topicIndex}>{topic}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BookNavigation;