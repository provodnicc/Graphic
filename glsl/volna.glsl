varying vec2 pos;
uniform sampler2D s_texture;
uniform float texture_width;
uniform float texture_height;


void main() {
    float tx = pos.x;
    float ty = pos.y;
    float dx = 1.0 / texture_width;
    float dy = 1.0 / texture_height;
    vec4 v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , 0 ) ).rgba;

    float temp = ty + sin((3.14 * tx*texture_width)/50.0)/100.0; //в синусе - на 

    // if(temp >0.0 && temp<dx)
    // {
    v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , temp ) ).rgba;
    // }else{
    //    v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , -temp ) ).rgba;

    // }
    gl_FragColor=v5;
}