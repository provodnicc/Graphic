varying vec2 pos;

void main() {
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    pos = gl_MultiTexCoord0.st;
}