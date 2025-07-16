import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

export default function FarmField() {
  return (
    <div style={{ width: '600px', height: '400px', border: '2px solid green' }}>
      <Canvas style={{ backgroundColor: '#222' }}>
        <ambientLight intensity={0.5} />
        <directionalLight position={[2, 5, 2]} />
        <mesh rotation={[0.4, 0.2, 0]}>
          <boxGeometry args={[2, 2, 2]} />
          <meshStandardMaterial color="orange" />
        </mesh>
        <OrbitControls />
      </Canvas>
    </div>
  );
}
